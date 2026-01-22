# Requires service account and keys to run or other access token- not created

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project = "project-49c604a8-3d62-43b5-9d9"
  region  = "us-central1"
  #credentials = file(var.credentials_json)
}

resource "google_storage_bucket" "auto-expire" {
  name          = "project-49c604a8-3d62-43b5-9d9-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}