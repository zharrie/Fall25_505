phone_number = int(input())

area_code = phone_number //10000000
prefix = phone_number // 10000
prefix = prefix % 1000
line_number = phone_number % 10000

print('(',area_code,')',' ',prefix,'-',line_number, sep="")