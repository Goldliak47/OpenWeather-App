[app]

android.sdk_tools_version = 35.0.0-rc1

# Title of your application
title = Weather App

# Package name
package.name = weatherapp

# Package domain (needed for Android/iOS packaging)
package.domain = com.example

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py

# Application versioning
version = 1.0.0

# Application requirements
requirements = python3,kivy,requests

# Android specific settings
android.permissions = INTERNET

# Supported orientation
orientation = portrait

# Presplash animation using Lottie format
android.presplash_lottie = "42369-weather-wind.json"

# Target Android API
android.api = 28

# Architecture to build for
android.arch = armeabi-v7a

# Allow backup for Android
android.allow_backup = True

[buildozer]

# Log level
log_level = 2

# Display warning if run as root
warn_on_root = 1
