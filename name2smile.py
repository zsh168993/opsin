import subprocess
cml="java -jar opsin-cli-2.7.0-jar-with-dependencies.jar -osmi input.txt output.txt"
nowtime = subprocess.run(cml, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print (nowtime.returncode)
