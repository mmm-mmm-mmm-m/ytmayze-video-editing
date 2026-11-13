# Release protocol

## Public experimental preview

The current scope permits publishing this experimental source preview while the license decision remains pending. Label the repository and README as experimental, and state that no license has been selected. Do not call it open source or claim MIT or other reuse rights. Add an actual license only after the owner makes that decision. See [License options](LICENSE-OPTIONS.md).

Stage a separate public copy of the eight skills; leave installed private skills unchanged. Rename the main skill `mayze-edit-video` to `ytmayze-video-editing` and apply the `mayze-` to `ytmayze-` mapping to its seven companions. Update frontmatter, triggers, and internal references, then check that links point to files present in the public tree.

Review the staged contents and images before publishing. Exclude raw project media, templates, private paths, chat or rollout identifiers, private quotations, machine metadata, credentials, and unrelated files. Include images only when their provenance and intended public use are clear. Do not treat publication as permission to access, source, or redistribute other media.

Run `python3 scripts/check_release.py` from the public tree. It checks the file/image allowlist, names, metadata, links, common private paths/chat IDs and credential signatures. It cannot decide whether prose reveals private context or a picture has suitable permissions; inspect those yourself. Keep private audit logs outside the repository. Review the staged diff before committing so excluded material never enters public Git history.

Describe the evidence accurately: the Saint Alien and Cranky Glow source tutorials were human rough-cut first and refined through many directed agent iterations. Source-style images are references, not proof that this release produced those edits. Run checks that fit the changes and report only what was actually verified; fresh-footage trials, before/after examples, and native-editor or listening review are not release gates.

## Later updates

For later skill updates, compare the existing public guidance with the changed private skills and carry over only the useful new lessons. Do not replace the public examples with private research or overwrite the public packaging with a raw directory copy. Update `VERSION` and `CHANGELOG.md`, prepare a scoped pull request, review its full diff for privacy and image provenance, and run CI. Merge within the user's then-current authorized scope once appropriate checks pass. Tag the merged revision and verify installation in a disposable project. Keep the installed private skills unchanged, and describe release status and verification accurately.
