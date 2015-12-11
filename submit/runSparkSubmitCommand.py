import os
import sys
import six

if  (len(sys.argv) < 2 or len(sys.argv) > 5):
  print("[*] Wrong use of command line arguments!")
  print("[*] This should be run as docker run [image-name] [location-of-jar-files] [mainClass] [master] [master-port]")
  print("[*] Ie.: docker run docker:image ~/api/jars/program.jar")
  print("[*] Or alternatively you can define the commands in your Dockerfile as follows:")
  print("[*] CMD [\"location-of-jar-files\",\"mainClass\",\"master\",\"master-port\"]")
  print("[*] mainClass, master and master-port are optional")
  print("[*] System will exit.")
  sys.exit(0)

jarLocation = sys.argv[1]

mainClass = "my.main.Application"

master = "spark-master"

masterport = "7077"

if len(sys.argv) > 2:
  mainClass = str(sys.argv[2])

if len(sys.argv) > 3:
  master = str(sys.argv[3])

if len(sys.argv) > 4:
  masterport = str(sys.argv[4])

print("[*] Building submit command with jar location '%s' and main class '%s'." % (jarLocation, mainClass))

cmd = "/spark/bin/spark-submit --class " + mainClass + " --master spark://" + master + ":" + masterport + " " + jarLocation

print("[x] Will execute command [%s]" % (cmd))

os.system(cmd)
