# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"14857","system":"readv2"},{"code":"6624","system":"readv2"},{"code":"56786","system":"readv2"},{"code":"59293","system":"readv2"},{"code":"34592","system":"readv2"},{"code":"58539","system":"readv2"},{"code":"7498","system":"readv2"},{"code":"107","system":"readv2"},{"code":"50159","system":"readv2"},{"code":"59467","system":"readv2"},{"code":"25903","system":"readv2"},{"code":"4175","system":"readv2"},{"code":"5587","system":"readv2"},{"code":"2128","system":"readv2"},{"code":"4490","system":"readv2"},{"code":"17177","system":"readv2"},{"code":"50148","system":"readv2"},{"code":"1398","system":"readv2"},{"code":"6594","system":"readv2"},{"code":"61769","system":"readv2"},{"code":"47014","system":"readv2"},{"code":"2062","system":"readv2"},{"code":"12469","system":"readv2"},{"code":"47670","system":"readv2"},{"code":"34699","system":"readv2"},{"code":"59378","system":"readv2"},{"code":"60245","system":"readv2"},{"code":"3068","system":"readv2"},{"code":"60573","system":"readv2"},{"code":"53846","system":"readv2"},{"code":"24637","system":"readv2"},{"code":"27967","system":"readv2"},{"code":"6504","system":"readv2"},{"code":"53750","system":"readv2"},{"code":"2782","system":"readv2"},{"code":"10263","system":"readv2"},{"code":"59504","system":"readv2"},{"code":"1370","system":"readv2"},{"code":"34144","system":"readv2"},{"code":"49789","system":"readv2"},{"code":"50147","system":"readv2"},{"code":"9678","system":"readv2"},{"code":"59082","system":"readv2"},{"code":"27113","system":"readv2"},{"code":"21854","system":"readv2"},{"code":"30392","system":"readv2"},{"code":"3881","system":"readv2"},{"code":"59377","system":"readv2"},{"code":"53749","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-fosphenytoin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-fosphenytoin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-fosphenytoin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
