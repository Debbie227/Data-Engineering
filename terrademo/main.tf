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
}