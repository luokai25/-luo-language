# Compiler work area

The first compiler milestone is a reference front end:

1. Source decoding and validation.
2. Lexer with source locations.
3. Parser and syntax tree.
4. Name and module resolution.
5. Type checking.
6. Typed intermediate representation.
7. Diagnostics and conformance tests.

The compiler implementation language has not yet been selected. The bootstrap compiler may use an existing language while preserving a path to self-hosting.

No fabricated Luo source syntax or placeholder glyphs are introduced here. The compiler must consume the approved native Luo writing system once glyph and text encoding design is finalized.
