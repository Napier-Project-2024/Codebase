package APIdemo

import (
	"encoding/json"
	"io/ioutil"
	"mind/core/framework/drivers/hexabody"
	"mind/core/framework/log"
	"mind/core/framework/skill"
	"net/http"
	"time"
)

type APIdemo struct {
	skill.Base
}

func NewSkill() skill.Interface {
	// Use this method to create a new skill.

	return &APIdemo{}
}

func (d *APIdemo) OnStart() {
	// Use this method to do something when this skill is starting.

	log.Info.Println("Starting Demo Sequence")

	if err := hexabody.Start(); err != nil {
		log.Error.Println("Failed to start hexabody:", err)
		return
	}

	stop := make(chan bool)

	go func() {
		for {
			select {
			case <-stop:
				log.Info.Println("Stopped Calling API")
				return
			default:
				callAPI()
			}

		}
	}()

	hexabody.StandWithHeight(100)

	// Assuming HEXA has 6 legs based on the design - this allows you to run the demo movement on any selection of leg(s)
	// Order the legs into groups
	legOrder := [][]int{{}, {3}} // Add the number of the leg you want the motion sequence to run on here

	for _, legs := range legOrder {

		done := make(chan struct{})

		for _, i := range legs {
			go func(leg int) {
				defer func() {
					done <- struct{}{}
				}()

				hexabody.MoveJoint(leg, 1, 10, 1000) //elbow
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 1, 170, 1000)
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 1, 10, 1000)
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 0, 35, 1000) //hip
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 0, 145, 1000)
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 0, 35, 1000)
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 2, 10, 1000) //toe
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 2, 160, 1000)
				time.Sleep(1 * time.Second)

				hexabody.MoveJoint(leg, 2, 10, 1000)
				time.Sleep(1 * time.Second)

				hexabody.StandWithHeight(100)
			}(i)
		}

		// Wait for all leg movements to complete
		for range legs {
			<-done
		}

		time.Sleep(2 * time.Second)

	}
	stop <- true
}

func (d *APIdemo) OnClose() {
	// Use this method to do something when this skill is closing.

	hexabody.Close()
	log.Info.Println("Demo closed")
}

func (d *APIdemo) OnConnect() {
	// Use this method to do something when the remote connected.
}

func (d *APIdemo) OnDisconnect() {
	// Use this method to do something when the remote disconnected.
}

func (d *APIdemo) OnRecvJSON(data []byte) {
	// Use this method to do something when skill receive json data from remote client.
}

func (d *APIdemo) OnRecvString(data string) {
	// Use this method to do something when skill receive string from remote client.
}

// Function to call the remote API and output the JSON string to the console
func callAPI() {
	// Set the URL from which the JSON will be retrieved
	url := "http://192.168.251.100:5000/returnValues" // The wifi network URL of the fastAPI instance

	// Issue an HTTP GET to the URL
	req, err := http.Get(url)

	// Handle any errors during the HTTP GET
	if err != nil {
		log.Info.Println("API Call Error:", err.Error())
		return
	}

	// Close the HTTP response body
	defer req.Body.Close()

	// Read in the response
	body, readErr := ioutil.ReadAll(req.Body)

	// Handle any HTTP response errors
	if readErr != nil {
		log.Info.Println("API Response Error:", err.Error())
		return
	}

	// Encode the response body as JSON
	json.Marshal(body)

	// Log the JSON to the console
	log.Info.Print(string(body))

}
