var orgTColor = '#595cd9';

function questionSelected(target, textColor) {
    var tbody = target.parentNode;
    var trs = tbody.getElementsByTagName('tr');
    
    for ( var i = 0; i < trs.length; i++ ) {
        if ( trs[i] != target ) {
        trs[i].style.color = textColor;
        } else {
        trs[i].style.color = orgTColor;
        }
    }
}