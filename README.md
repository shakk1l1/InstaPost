# InstaPost

A Python prototype for selecting photographs from a local folder, generating
captions from image metadata, and posting through `instagrapi`. A local database
records image paths to help track previously processed photographs.

## Components

| File | Role |
| --- | --- |
| `main.py` | Application entry point and posting workflow |
| `Commands.py` | Interactive commands and folder-path configuration |
| `login_user.py` | Account login prompts |
| `post.py` | Image selection, preview, and upload helpers |
| `caption_generation.py`, `get_metadata.py` | Caption and metadata handling |
| `database.py` | Local image-record database |
| `path.py` | Local image-folder setting |

## Prototype status

The current entry point awaits helpers that are defined as synchronous
functions. That mismatch needs to be corrected before treating the full
workflow as usable. Compatibility with the current Instagram service has not
been verified, and this README does not claim a working deployment.

The code depends on third-party packages, including `instagrapi` and Pillow;
a complete pinned environment is not supplied. Inspect the module imports and
resolve the entry-point issues before attempting a run with an account.

## Interface

The command dispatcher includes `help`, `connect`, `path`, `random`, `specific`,
`get`, `add`, `list`, and `exit`. Folder configuration is handled through `path`
and then `new`. These describe the implemented command branches, not verified
end-to-end behaviour.

## Image handling

**The `get` preview flow can delete a local image when you answer `y` to its
“add and delete” prompt.** Use copies of photographs when experimenting.

The upload helper currently uploads and records the image path; it does not
itself remove the image, despite an older docstring describing removal.
Keep this distinction in mind when reviewing the code.

No account login, upload, or deletion was executed for this documentation update.
