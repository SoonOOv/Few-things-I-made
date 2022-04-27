function digital_root(n) {
  if (String(n).length == 1){
    return n
  }
  let s = String(n)
  let sum = 0
  for (let i = 0;i < s.length;i++){
    sum += Number(s.charAt(i))
  }
  return digital_root(sum)
}
