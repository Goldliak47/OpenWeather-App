[app]
title = MyWeatherApp
package.name = myweatherapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Kivy version required by the app
osx.python_version = 3.8.10

# Android specific settings
osx.python_version = 3.8.10
android.permissions = INTERNET

# Add additional requirements if needed
requirements = python3,kivy,requests

# Specify Android SDK version
android.api = 30

# Specify Android SDK tools version
android.sdk = 30.0.3

# Specify Android NDK version
android.ndk = 21.4.7075529
