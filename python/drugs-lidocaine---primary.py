# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"51035","system":"readv2"},{"code":"14157","system":"readv2"},{"code":"2520","system":"readv2"},{"code":"48925","system":"readv2"},{"code":"2305","system":"readv2"},{"code":"61455","system":"readv2"},{"code":"48897","system":"readv2"},{"code":"49496","system":"readv2"},{"code":"3667","system":"readv2"},{"code":"14510","system":"readv2"},{"code":"39097","system":"readv2"},{"code":"39971","system":"readv2"},{"code":"18385","system":"readv2"},{"code":"51442","system":"readv2"},{"code":"5225","system":"readv2"},{"code":"118","system":"readv2"},{"code":"48512","system":"readv2"},{"code":"13152","system":"readv2"},{"code":"51331","system":"readv2"},{"code":"20600","system":"readv2"},{"code":"48453","system":"readv2"},{"code":"20882","system":"readv2"},{"code":"26894","system":"readv2"},{"code":"25838","system":"readv2"},{"code":"3030","system":"readv2"},{"code":"5831","system":"readv2"},{"code":"17047","system":"readv2"},{"code":"11809","system":"readv2"},{"code":"18043","system":"readv2"},{"code":"55542","system":"readv2"},{"code":"28824","system":"readv2"},{"code":"7635","system":"readv2"},{"code":"41043","system":"readv2"},{"code":"48865","system":"readv2"},{"code":"42789","system":"readv2"},{"code":"51336","system":"readv2"},{"code":"18781","system":"readv2"},{"code":"57244","system":"readv2"},{"code":"41972","system":"readv2"},{"code":"24901","system":"readv2"},{"code":"12971","system":"readv2"},{"code":"23508","system":"readv2"},{"code":"40451","system":"readv2"},{"code":"61805","system":"readv2"},{"code":"55182","system":"readv2"},{"code":"12982","system":"readv2"},{"code":"56373","system":"readv2"},{"code":"55196","system":"readv2"},{"code":"56408","system":"readv2"},{"code":"14451","system":"readv2"},{"code":"40969","system":"readv2"},{"code":"13140","system":"readv2"},{"code":"54854","system":"readv2"},{"code":"14418","system":"readv2"},{"code":"2859","system":"readv2"},{"code":"4366","system":"readv2"},{"code":"51733","system":"readv2"},{"code":"49845","system":"readv2"},{"code":"48694","system":"readv2"},{"code":"39453","system":"readv2"},{"code":"36415","system":"readv2"},{"code":"48954","system":"readv2"},{"code":"53914","system":"readv2"},{"code":"31331","system":"readv2"},{"code":"16927","system":"readv2"},{"code":"13922","system":"readv2"},{"code":"48390","system":"readv2"},{"code":"48466","system":"readv2"},{"code":"35043","system":"readv2"},{"code":"27692","system":"readv2"},{"code":"5796","system":"readv2"},{"code":"19822","system":"readv2"},{"code":"51329","system":"readv2"},{"code":"502","system":"readv2"},{"code":"47658","system":"readv2"},{"code":"29608","system":"readv2"},{"code":"26500","system":"readv2"},{"code":"30149","system":"readv2"},{"code":"51330","system":"readv2"},{"code":"51734","system":"readv2"},{"code":"30497","system":"readv2"},{"code":"48395","system":"readv2"},{"code":"14855","system":"readv2"},{"code":"48450","system":"readv2"},{"code":"40332","system":"readv2"},{"code":"57141","system":"readv2"},{"code":"48391","system":"readv2"},{"code":"48714","system":"readv2"},{"code":"17251","system":"readv2"},{"code":"4893","system":"readv2"},{"code":"32304","system":"readv2"},{"code":"25536","system":"readv2"},{"code":"15320","system":"readv2"},{"code":"53014","system":"readv2"},{"code":"43571","system":"readv2"},{"code":"3134","system":"readv2"},{"code":"37593","system":"readv2"},{"code":"61179","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-lidocaine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-lidocaine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-lidocaine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
