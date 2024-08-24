\c 10000 10000

data: read0 `:/home/harsshal/competitions/AdventOfCode/2023/11_Cosmic/input_1.txt;
show data;

/process row function to check the lines which have no # and add a line

expand:(flip{x where 1+0=sum'[x="#"]}@)/[2;]
expand data

expand2:(flip{x where 1+0=sum'[x="#"]}@)/[0;]
expand2 data


process_row:{[row]
    {x where 1+0=sum'[x="#"]}row;
    }

/process_row each data;


\\