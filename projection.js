const proj4 = require("proj4");
const fs = require("fs");

const NAD83Projection =
  'PROJCS["NAD83 / Massachusetts Mainland",GEOGCS["NAD83",DATUM["North_American_Datum_1983",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],AUTHORITY["EPSG","6269"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4269"]],UNIT["metre",1,AUTHORITY["EPSG","9001"]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["standard_parallel_1",49],PARAMETER["standard_parallel_2",77],PARAMETER["latitude_of_origin",63.390675],PARAMETER["central_meridian",-91.866667],PARAMETER["false_easting",6200000],PARAMETER["false_northing",3000000],AUTHORITY["EPSG","26986"],AXIS["X",EAST],AXIS["Y",NORTH]]';

const files = ["hwy", "ramp", "class_code", "cross", "searcher_result"];
console.log(
  proj4(NAD83Projection).inverse([8442845.462899998, 1579043.0229000002])
);
// [-2690666.2977344505, 3662659.885459918]

function converter(file_name) {
  json_path = "./" + file_name + "/" + file_name + ".json";
  fs.readFile(json_path, (err, data) => {
    var coords = [];
    if (err) throw err;
    var road_data = JSON.parse(data);

    for (let i = 0; i < road_data.length; i++) {
      x = road_data[i][0];
      y = road_data[i][1];
      coord = proj4(NAD83Projection).inverse([x, y]);
      coords.push(coord);
    }

    var result_path = "./" + file_name + "/" + file_name + "_coords.json";
    var myJSON = JSON.stringify(coords);
    fs.writeFile(result_path, myJSON, err => {
      if (err) throw err;
    });
    console.log("completed");
  });
}

const test_files = ["test_bc_ab", "test_on", "test_qb", "test_yk", "test_ss"];

function converter_test(file_name) {
  json_path = "./test/" + file_name + ".json";
  fs.readFile(json_path, (err, data) => {
    var coords = [];
    if (err) throw err;
    var road_data = JSON.parse(data);

    for (let i = 0; i < road_data.length; i++) {
      x = road_data[i][0];
      y = road_data[i][1];
      coord = proj4(NAD83Projection).forward([y, x]);
      coords.push(coord);
    }

    var result_path = "./test/test_QGIS/" + file_name + "_NAD83.json";
    var myJSON = JSON.stringify(coords);
    fs.writeFile(result_path, myJSON, err => {
      if (err) throw err;
    });
    console.log("completed");
  });
}

// converter(test_files[3]);
