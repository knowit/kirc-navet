const parseStyle = (json) => {
    return Object.entries(json).map(([k, v]) => `${k}:${v}`).join(';');
}


const testobj = {"color": "red", "size": 28, "bgcolor" : "blue", "italic":true, "bold": true};

console.log(parseStyle(testobj));




