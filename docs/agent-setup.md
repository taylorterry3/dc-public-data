# Agent setup

## Personal skills

Matt Pocock's skills are installed per user in `~/.codex/skills/`. Keep skill implementations outside this repository.

Source: [mattpocock/skills](https://github.com/mattpocock/skills), revision `5863806dd4e15c63174bee4e7515a4256792ecfa`. The installation includes 31 skills from `skills/engineering`, `skills/productivity`, and `skills/misc`; it excludes `skills/in-progress`.

A fresh checkout does not install personal skills. Use Codex's skill-installer with that repository and revision, selecting the skill folders above and the default global destination.

## Project command permissions

`.codex/rules/claude-import.rules` contains 43 command allowances and five denials imported from the local Claude settings. Codex loads project rules for trusted projects at startup; restart after changing them.

These rules permit matching commands outside the sandbox. Several allowances, including `git` and `uv`, are broad. The denials use argument prefixes, so `git push --force origin main` is blocked but `git push origin main --force` and `--force-with-lease` are not covered.

Claude's file-read exclusions, editing permissions, and web-tool permissions are not represented by command rules. Unrestricted Python, Node, and Bash allowances were omitted. These omissions do not enforce file confidentiality: allowed commands can still read files or launch other programs.

## Remaining workflow configuration

The skills' per-repository workflow setup is still pending: choose the issue tracker and triage labels, record domain-document conventions under `docs/agents/`, and link those conventions from the existing `CLAUDE.md` using `setup-matt-pocock-skills`.
