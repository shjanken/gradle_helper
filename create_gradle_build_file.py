#!/usr/bin/env python

# create gradle.build by python

from select_language import Language
from select_ide import SelectIDE

# get the language  result
lan = Language()
lang_result = lan.get_input()


# get the selected_ide
ideSelector = SelectIDE()
ide_result = ideSelector.get_input()

file_text = """
repositories {
	maven {
		url "http://maven.oschina.net/content/groups/public/"
	}
}

dependencies {
    testCompile group: 'junit', name: 'junit', version: '4.+'
}

task "printDirs" << {
    description "print the directories"
    sourceSets.all { set ->
        set.allSource.srcDirs.each { println it }
    }
}

task "mkSourceDirs" << {
    description "create directories"
    sourceSets.all { set ->
        set.allSource.srcDirs.each { it.mkdirs() }
    }
}

"""

# wirte the file
with open("build.gradle","w") as buildfile:
    buildfile.write( "apply plugin: "+ ide_result + "\n")
    buildfile.write( "apply plugin: "+ lang_result + "\n")
    buildfile.write(file_text)
