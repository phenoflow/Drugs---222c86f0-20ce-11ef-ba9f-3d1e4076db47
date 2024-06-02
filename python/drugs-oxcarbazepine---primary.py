# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"55904","system":"readv2"},{"code":"46972","system":"readv2"},{"code":"59746","system":"readv2"},{"code":"53893","system":"readv2"},{"code":"59429","system":"readv2"},{"code":"17429","system":"readv2"},{"code":"61377","system":"readv2"},{"code":"45903","system":"readv2"},{"code":"12931","system":"readv2"},{"code":"7020","system":"readv2"},{"code":"32900","system":"readv2"},{"code":"14199","system":"readv2"},{"code":"59428","system":"readv2"},{"code":"34904","system":"readv2"},{"code":"59745","system":"readv2"},{"code":"11696","system":"readv2"},{"code":"432","system":"readv2"},{"code":"51760","system":"readv2"},{"code":"7021","system":"readv2"},{"code":"43417","system":"readv2"},{"code":"5977","system":"readv2"},{"code":"40404","system":"readv2"},{"code":"1158","system":"readv2"},{"code":"3569","system":"readv2"},{"code":"37058","system":"readv2"},{"code":"13112","system":"readv2"},{"code":"52840","system":"readv2"},{"code":"12880","system":"readv2"},{"code":"21441","system":"readv2"},{"code":"13524","system":"readv2"},{"code":"53492","system":"readv2"},{"code":"59887","system":"readv2"},{"code":"59696","system":"readv2"},{"code":"53188","system":"readv2"},{"code":"43451","system":"readv2"},{"code":"6552","system":"readv2"},{"code":"15082","system":"readv2"},{"code":"37800","system":"readv2"},{"code":"17978","system":"readv2"},{"code":"60405","system":"readv2"},{"code":"18762","system":"readv2"},{"code":"54445","system":"readv2"},{"code":"59697","system":"readv2"},{"code":"4913","system":"readv2"},{"code":"34370","system":"readv2"},{"code":"18763","system":"readv2"},{"code":"32931","system":"readv2"},{"code":"26012","system":"readv2"},{"code":"28345","system":"readv2"},{"code":"4066","system":"readv2"},{"code":"58515","system":"readv2"},{"code":"26902","system":"readv2"},{"code":"45941","system":"readv2"},{"code":"59211","system":"readv2"},{"code":"34958","system":"readv2"},{"code":"2824","system":"readv2"},{"code":"2085","system":"readv2"},{"code":"5449","system":"readv2"},{"code":"2388","system":"readv2"},{"code":"59430","system":"readv2"},{"code":"18011","system":"readv2"},{"code":"60181","system":"readv2"},{"code":"56734","system":"readv2"},{"code":"4982","system":"readv2"},{"code":"41726","system":"readv2"},{"code":"596","system":"readv2"},{"code":"46888","system":"readv2"},{"code":"59038","system":"readv2"},{"code":"18567","system":"readv2"},{"code":"652","system":"readv2"},{"code":"49833","system":"readv2"},{"code":"12932","system":"readv2"},{"code":"40403","system":"readv2"},{"code":"60133","system":"readv2"},{"code":"6436","system":"readv2"},{"code":"61143","system":"readv2"},{"code":"47294","system":"readv2"},{"code":"2823","system":"readv2"},{"code":"30763","system":"readv2"},{"code":"17428","system":"readv2"},{"code":"57726","system":"readv2"},{"code":"48397","system":"readv2"},{"code":"30509","system":"readv2"},{"code":"60187","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-oxcarbazepine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-oxcarbazepine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-oxcarbazepine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
