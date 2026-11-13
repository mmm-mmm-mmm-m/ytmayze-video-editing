# EffectCraft native transfer

This optional editor-specific workflow does not establish compatibility with every editor version. Discover the current supported import mechanism and schema.

From this skill directory:

```sh
python3 scripts/inspect_native_preset.py /path/to/your-preset.ecpreset
```

The inspector reads animation-preset marker 1, reports effect order and integer key-time extents, and lists channels with expressions without executing them. It does not import effects or establish appearance, timing or sound quality.

Supply `--ticks-per-second` only from evidence about the actual format. `--fps` additionally reports exact frame coordinates. For a file confirmed to use 254016000000 ticks/second at 30 fps:

```sh
python3 scripts/inspect_native_preset.py /path/to/your-preset.ecpreset --ticks-per-second 254016000000 --fps 30
```

That timebase is a known example, not an inferred default. Fractional frame rates such as `24000/1001` are accepted. Key-time bounds are distinct from the intended adjustment-layer display window.

A preset may contain a complete effects stack; repeated application can compound it. Use a separate instance or reconcile existing effects while preserving the creator's grade, crop and motion. A return to preset baseline may still include grade/glow rather than the untreated image.

Adapt centers and margins to destination geometry and subject. Keep motion separate from brightness/color/glow. Preserve elapsed seconds unless a musical retime is intended, then quantize once at the destination frame rate.

Prefer supported import to direct host-file mutation. For programmatic edits, inspect the current schema, allocate fresh IDs and verify source/parent/matte references. Reopen a separate revision and review loading, seams, motion and audio before claiming reuse. Do not run a historical project writer as a discovery step.
