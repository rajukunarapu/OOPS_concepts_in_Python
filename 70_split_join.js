
// 1. Split = Split the all string into array elements
// str_name.split(seperator,limit)

var str = "john mike bob nick"
var var_1 = str.split(" ")    // It checks the string, Where it has spaces it treats as new element of an array in result.
console.log(var_1)

var str1 = "haun-rockey-jawid-itachi"
var var_2 = str1.split("-", 3)  // It checks the string, Where it has hypen it treats as new element of an array in result. limit is 3 elements
console.log(var_2)


// 2.join = Join the array elements and returns as string
//arr_name.join(seperator)
var arr_1 = ["Naruto", "yellow flash", "kakashi"]
var var_4 = arr_1.join()      // Defaultly, seperated by comma
var var_3 = arr_1.join(" ")   // Elements seperated by space.
console.log(var_3)
console.log(var_4)