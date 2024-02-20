[app]
title = MyWeatherApp
package.name = myweatherapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

[buildozer]
# Set the buildozer directory to store dependencies
directory = /home/runner/.buildozer

# Android specific settings
android.permissions = INTERNET
android.accept_licenses = True