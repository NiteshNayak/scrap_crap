# This script is to remove all the cap before the actual document

infile = '/Users/nnayak/Desktop/cert.txt'
outfile = '/Users/nnayak/Desktop/clean.txt'

delete_list = ['mp        plugin_cloud_services.log          2019-03-18 04:00:02',' ']

fin = open(infile)
fout = open(outfile,'w')

for line in fin:
    for word in delete_list:
        line = line.replace(word,'')
    fout.write(line)

fin.close()
fout.close()
