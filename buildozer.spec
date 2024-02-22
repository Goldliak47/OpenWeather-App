[app]

# Title of your application
title = Weather App

# Package name
package.name = weatherapp

# Package domain (needed for Android/iOS packaging)
package.domain = com.example

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application versioning
version = 1.0.0

# Application requirements
requirements = python3,kivy,requests,android

# Android specific settings
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Supported orientation
orientation = portrait

# Target Android API
android.api = 33

android.minapi = 21

# Android SDK and NDK
android.sdk = /path/to/your/android-sdk
android.ndk = 21b
android.sdk_tools_version = 35.0.0-rc1

# Architecture to build for
android.arch = armeabi-v8a

# Allow backup for Android
android.allow_backup = True

# Whether to use AndroidX libraries
android.use_androidx = True

# Android logcat filters to use (uncomment to enable)
#android.logcat_filters = *:S python:D

# Whether to copy the Python interpreter and libraries to the APK
android.strip_libraries = True

[buildozer]

# Log level
log_level = 2

# Display warning if run as root
warn_on_root = 1
