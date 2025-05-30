% {{ metadata.title }}
% {{ metadata.author }}
% {{ metadata.generation_date }}

# {{ metadata.title }}

## Purpose
{{ content.purpose }}

## Scope
{{ content.scope }}

{{ include("common/test_references.md") }}
{{ include("common/test_abbrev_and_def.md") }}

{{ include(content.main_file) }}
