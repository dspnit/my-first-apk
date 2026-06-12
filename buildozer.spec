[app]
title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py

requirements = python3,kivy==2.1.0,numpy
[buildozer]
log_level = 2
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
