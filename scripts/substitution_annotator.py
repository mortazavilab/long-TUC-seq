from optparse import OptionParser
import re

def getOptions():
    parser = OptionParser()
    parser.add_option("--input","-i", dest = "infile", help = "Input filtered sam file",
                      metavar = "FILE", type = "string", default = "")

    parser.add_option("--output_pre","-o", dest = "outfile", help = "Output prefix for sub samfiles",
                      metavar = "FILE", type = "string", default = "")
    (options, args) = parser.parse_args()
    return options


def main():
    options = getOptions()
    sam_file = options.infile
    out_prefix = options.outfile
    header = []
    transcripts_0TC = []
    transcripts_6TC = []
    transcripts_20TC = []
    transcripts_30TC = []
    f_log = open(str(out_prefix + "_SNP_log.txt"),"w")
    f_out = open(str(out_prefix + "_SNP.txt"),"w")
    f_out.write("\t".join(("name","TT","TC","TG","TA","CT","CC","CG","CA","GT","GC","GG","GA","AT","AC","AG","AA"))+"\n")
    with open(sam_file, 'r') as f:
       for l,line in enumerate(f):
          line = line.strip()
          if line.startswith('@'):
             header.append(line)
          else:
             fields = line.split("\t")
             name = fields[0]
             flag = int(fields[1])
             seq = fields[9]
             cs_field = [m for m in fields[11:len(fields)] if m.startswith("cs")]


             TC=0

             if len(cs_field) == 0:
                f_log.write("No CS field \n")
                continue
             cs = cs_field[0].split(":Z:")[1]

             if flag == 0 or flag == 16:
                TC = cs.count('*tc')
                TG = cs.count('*tg')
                TA = cs.count('*ta')
                CT = cs.count('*ct')
                CG = cs.count('*cg')
                CA = cs.count('*ca')
                GT = cs.count('*gt')
                GC = cs.count('*gc')
                GA = cs.count('*ga')
                AT = cs.count('*at')
                AC = cs.count('*ac')
                AG = cs.count('*ag')
                tT = seq.count('T')-CT-GT-AT+TC+TG+TA
                tC = seq.count('C')-TC-GC-AC+CT+CG+CA
                tG = seq.count('G')-CG-TG-AG+GC+GT+GA
                tA = seq.count('A')-CA-GA-TA+AC+AG+AT
                f_out.write("\t".join((str(name),str(tT),str(TC),str(TG),str(TA),str(CT),str(tC),str(CG),str(CA),str(GT),str(GC),str(tG),str(GA),str(AT),str(AC),str(AG),str(tA)))+"\n")

             if TC > 30:
                transcripts_30TC.append(line)
             elif TC > 20:
                transcripts_20TC.append(line)
             elif TC > 6:
                transcripts_6TC.append(line)
             elif flag  == 0 or flag == 16:
                transcripts_0TC.append(line)

    f.close()
    f_log.close()
    f_out.close()
    with open(str(out_prefix + "_0.sam"),"w+") as f:
         for i in range(len(header)):
             f.write(header[i]+"\n")
         for i in range(len(transcripts_0TC)):
             f.write(transcripts_0TC[i]+"\n")
         for i in range(len(transcripts_6TC)):
             f.write(transcripts_6TC[i]+"\n")
         for i in range(len(transcripts_20TC)):
             f.write(transcripts_20TC[i]+"\n")
         for i in range(len(transcripts_30TC)):
             f.write(transcripts_30TC[i]+"\n")
    f.close()
    with open(str(out_prefix + "_6.sam"),"w+") as f:
         for i in range(len(header)):
             f.write(header[i]+"\n")
         for i in range(len(transcripts_6TC)):
             f.write(transcripts_6TC[i]+"\n")
         for i in range(len(transcripts_20TC)):
             f.write(transcripts_20TC[i]+"\n")
         for i in range(len(transcripts_30TC)):
             f.write(transcripts_30TC[i]+"\n")
    f.close()
    with open(str(out_prefix + "_20.sam"),"w+") as f:
         for i in range(len(header)):
             f.write(header[i]+"\n")
         for i in range(len(transcripts_20TC)):
             f.write(transcripts_20TC[i]+"\n")
         for i in range(len(transcripts_30TC)):
             f.write(transcripts_30TC[i]+"\n")
    f.close()

    with open(str(out_prefix + "_30.sam"),"w+") as f:
         for i in range(len(header)):
             f.write(header[i]+"\n")
         for i in range(len(transcripts_30TC)):
             f.write(transcripts_30TC[i]+"\n")
    f.close()



if __name__ == '__main__':

   main()



