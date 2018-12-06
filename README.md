# Dice Image API
A simple api made from to serve the faces of a dice in the form of images.

### API endpoint
http://saiyerniakhil.pythonanywhere.com

Please do note that both the images and the API is hosted on a free tier thus, low speeds.The images available might be improved in future 

### How to use it?
You can use any common way of making an api request

  #### Example - jQuery
  ```
   $.get("API_END_POINT", function (obj) {
                                  // you can use the object passed into the parameters of the anonymous function above
                                  // to fetch details from server
                              });
  ```
  #### Structure
    ```
    {
    "1": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098990/1.png",
    "2": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098990/2.png",
    "3": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098991/3.png",
    "4": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098990/4.png",
    "5": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098991/5.png",
    "6": "https://res.cloudinary.com/dibjkdnch/image/upload/v1544098991/6.png"
    }
    ```
All the images were hosted on [cloudinary](www.cloudinary.com)
