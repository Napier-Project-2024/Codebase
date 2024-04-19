# Demonstration of Hexasense API Usage

This demo HEXA project shows the basic operation of the Hexasense API in the context of a Mind SDK Go script.
To execute this demo, the "APIdemo" folder and all it's contents should be copied to your ```~/go/src/mindsdk/``` directory and executed from inside the APIdemo directory using the command ```mind build && mind pack && mind run```

The Go script itself is found at ```/APIdemo/src/apidemo.go```

This simple script performs a full range motion on each of the specified leg's joints whilst calling the Hexasense API via HTTP and printing the API response JSON string to the console, a shown in the sample output below.
![Sample Console Output](./images/example-console-output.png)

## The Example callAPI() Function

This function demonstrates how to call the API from a Go script and store the response in a JSON format.
The example also prints this response to the console.

The callAPI function makes use of the "http", "ioutil", and "json" libraries which are imported alongside the required Mind SDK libraries as shown below.

```go
import (
	
	"mind/core/framework/drivers/hexabody"
	"mind/core/framework/log"
	"mind/core/framework/skill"
	"time"
	"net/http"
	"io/ioutil"
	"encoding/json"
)
```

The callAPI function begins by declaring the URL that the API calls are made to.
This can be changed to match your specific implementation of the API.

```go
// Set the URL from which the JSON will be retrieved
	url := "http://192.168.251.100:5000/returnValues" // The wifi network URL of the fastAPI instance
```

The function then issues an HTTP GET request to the specified URL, storing the request response and any error messsage.

```go
// Issue an HTTP GET to the URL
	req, err := http.Get(url)
```

The following IF statement handles any errors that are returned, printing the error message to the console.

```go
	// Handle any errors during the HTTP GET
	if err != nil {
		log.Info.Println("API Call Error:", err.Error())
		return
	}
```

When no errors are returned, the function then closes the HTTP response body.

```go
	// Close the HTTP response body
	defer req.Body.Close()
```

The HTTP response body is then read into a "body" variable and any errors reading the body are stored.

```go
	// Read in the response body
	body, readErr := ioutil.ReadAll(req.Body)
```

If an error is detected while reading in the HTTP response body, the error is printed to the console.

```go
	// Handle any HTTP response errors
	if readErr != nil {
		log.Info.Println("API Response Error:", err.Error())
		return
	}
```

The HTTP response body is then encoded into the JSON format.

```go
	// Encode the response body as JSON
	json.Marshal(body)
```

This JSON string can now be printed to the console.

```go
	// Log the JSON to the console
	log.Info.Print(string(body))
```


