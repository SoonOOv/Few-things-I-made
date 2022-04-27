function f(x, y) {
    let num = 1;
    let side = 1;
    let xc = 0, yc = 0
    let direction = 1
    let count = 0
    let sideStep = 0
    while (xc !== x || yc !== y) {
        if (count == 2) {
            count = 0
            side++
        }
        if (sideStep == side) {
            sideStep = 0
            count++
            direction == 4 ? direction = 1 : direction++
        }
        switch (direction) {
            case 1:
                xc++;
                break;
            case 2:
                yc++;
                break;
            case 3:
                xc--;
                break;
            case 4:
                yc--;
                break;
        }
        num++
        sideStep++
    }
    return num
}
