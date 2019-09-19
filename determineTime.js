function updateDate(lastTime){
    let nowDate = Date()  //获取当前的时间
    let beforeDate = new Date(lastTime)  //将传入的时间格式化
    let parseBeforeDate = Date.parse(beforeDate)  //将传入的时间转化成时间戳
    let parseNowDate = Date.parse(nowDate)  // 将当前的时间转化成时间戳

    let remainDate = parseNowDate - parseBeforeDate  //两个时间戳相减

    let remainD = remainDate/1000/60/60  //将时间戳转化成小时
    if(remainD > 24){  // 判断如果大于24小时就返回true  小于24小时返回false
        return true
    }else{
        return false
    }
}
