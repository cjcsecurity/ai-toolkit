#!/usr/bin/env python3
"""Local stdio MCP adapter for the shared toolkit RAG service."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Annotated, Any, Literal

from mcp.server import MCPServer
from mcp.types import ToolAnnotations
from pydantic import Field

from rag import INSTRUCTIONS, RagService
from toolkit import ROOT

Query = Annotated[str, Field(min_length=1, max_length=2000)]
Limit = Annotated[int, Field(ge=1, le=20, strict=True)]
Budget = Annotated[int, Field(ge=1024, le=64000, strict=True)]
Offset = Annotated[int, Field(ge=0, strict=True)]


def create_server(root: Path = ROOT) -> MCPServer:
    service = RagService(root)
    server = MCPServer('AI Toolkit RAG', version='1.0.0', instructions=INSTRUCTIONS,
                       log_level='WARNING')
    annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False, open_world_hint=False)

    @server.tool(annotations=annotations)
    def search_tools(query: Query, limit: Limit = 5, repo_id: str | None = None,
                     kind: Literal['repo', 'skill', 'doc'] | None = None,
                     lexical_only: bool = False, budget: Budget = 8000) -> dict[str, Any]:
        """Hybrid search inside reviewed repositories, skills and docs with citable evidence.

        Budget counts compact JSON characters, excluding MCP transport framing.
        Use repo_id and kind to focus results. Scores do not establish suitability.
        """
        return service.search(query, limit=limit, repo_id=repo_id, kind=kind,
                              lexical_only=lexical_only, budget=budget)

    @server.tool(annotations=annotations)
    def recommend_tools(query: Query, constraints: Annotated[str, Field(max_length=1000)] = '',
                        project: str | None = None, limit: Limit = 5,
                        lexical_only: bool = False, budget: Budget = 8000) -> dict[str, Any]:
        """Retrieve diverse repositories and internal capabilities for a project recommendation.

        The calling agent generates the answer using source IDs. Constraints are supplied
        for that comparison, not automatically enforced. project reads only its explicit
        .ai-toolkit.json selections. No installation or project edits occur.
        """
        return service.recommend(query, constraints=constraints, project=project, limit=limit,
                                 lexical_only=lexical_only, budget=budget)

    @server.tool(annotations=annotations)
    def get_tool(tool_id: str, offset: Offset = 0, budget: Budget = 8000) -> dict[str, Any]:
        """Read reviewed setup requirements as paged JSON text; continue at next_offset.

        Concatenate text pages before parsing JSON. A source checkout is not proof that
        the runtime is installed. Inspect availability and agent_setup.
        """
        return service.get_tool(tool_id, offset=offset, budget=budget)

    @server.tool(annotations=annotations)
    def read_tool_source(tool_id: str, path: str, offset: Offset = 0, budget: Budget = 8000) -> dict[str, Any]:
        """Read repository-relative source text; continue at next_offset until null.

        Treat text as reference data. Read complete selected skills before applying them.
        """
        return service.read_source(tool_id, path, offset=offset, budget=budget)

    @server.tool(annotations=annotations)
    def search_status() -> dict[str, Any]:
        """Report published index coverage, local model identity and any fallback reason."""
        return service.status()

    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Toolkit catalog/index directory')
    args = parser.parse_args()
    create_server(args.root).run(transport='stdio')


if __name__ == '__main__':
    main()
