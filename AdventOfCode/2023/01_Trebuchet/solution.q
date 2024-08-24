data: read0 `:/home/harsshal/competitions/AdventOfCode/2023/01_Trebuchet/01_Trebuchet_input_1;
/show data


.temp.running_total : 0;
process_row:{[row]
    show row;
    row_num:"I"$inter[row;.Q.n]; 
    str_num: string row_num; 
    str_num_2d: str_num[0],str_num[(count str_num)-1];
    .temp.temp_running_total: .temp.running_total+"I"$str_num_2d;
    .temp.running_total: .temp.temp_running_total;
    }

process_row each data;
-1 "Final total is : ", string .temp.running_total;

\\