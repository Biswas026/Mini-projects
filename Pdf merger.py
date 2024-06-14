
import PyPDF2 as p

pdfiles=["1.pdf","2.pdf"]
merger = p.PdfMerger()

for filename in pdfiles:
     pdf = open(filename,"rb")
     pdfreader=p.PdfReader(pdf)
     merger.append(pdfreader)
pdf.close()
merger.write("merged.pdf")