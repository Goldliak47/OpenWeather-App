[app]
title = MyWeatherApp
package.name = myweatherapp
package.domain = com.example
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

[buildozer]
# Set the buildozer directory to store dependencies
directory = /home/runner/.buildozer

# Android specific settings
package.name = myweatherapp
package.domain = com.example
package.source = .

# Specify the version of Build-Tools
android.build_tools_version = 30.0.3

# Android permissions
android.permissions = INTERNET

# Kivy version to use in the APK
# (This version should match the one specified in [app] section)
p4a.branch = 2.0.0
