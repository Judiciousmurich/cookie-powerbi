
let powerbi = require('powerbi-visuals-tools');

const myVisual = {
    
    settings: {
        visuals: {
            title: 'My Custom Visual'
        }
    },

    updateDataView: function(dataView) {
      
        let data = dataView.table.rows;
        console.log("Data for custom visual:", data);
    }
};

module.exports = myVisual;
