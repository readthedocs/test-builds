terraform {
  required_providers {
    readthedocs = {
      source = "BarnabyShearer/readthedocs"
    }
  }
}

provider "readthedocs" {
  # Define READTHEDOCS_TOKEN with direnv instead
  # token = ""
}

resource "readthedocs_project" "test-builds" {
  name                    = "test-builds"
  repository              = "https://github.com/readthedocs/test-builds.git"
  analytics_disabled      = false
  default_branch          = "py3.8"
  external_builds_enabled = false
  programming_language    = "words"
  show_version_warning    = true
  single_version          = false
}
