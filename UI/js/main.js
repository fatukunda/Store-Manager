const sellBtn = $('.sell');
const categorizeBtn = $('.categorize');
let categorizeRow = $('.toggle-categorize')
let quantityRow = $('.toggle-sell');
if(sellBtn.click(() => {
    categorizeRow.hide();
    quantityRow.show();
}));
if(categorizeBtn.click(() => {
    quantityRow.hide();
    categorizeRow.show();
}));

