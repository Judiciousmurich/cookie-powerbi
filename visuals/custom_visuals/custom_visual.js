// Simple Power BI custom visual template using the Power BI custom visual SDK
let powerbi = require('powerbi-visuals-tools');

const myVisual = {
    // Power BI visual configuration
    settings: {
        visuals: {
            title: 'My Custom Visual'
        }
    },

    updateDataView: function(dataView) {
        // Process the data and render the visual
        let data = dataView.table.rows;
        console.log("Data for custom visual:", data);
    }
};

module.exports = myVisual;
