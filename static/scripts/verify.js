const inputs=document.querySelectorAll("input"),
             button=document.querySelector("button"); 
           
             inputs.forEach((input,index1) => {
                input.addEventListener("keyup", () =>
                {         
                    const currentInput=input,
                           nextInput =input.nextElementSibling,
                           prevInput=input.previousElementSibling;
                           
                           if(currentInput.value.length > 1)
                           {
            
                            currentInput.value ="";
                            return;
                           }
                            
                           if(nextInput && nextInput.hasAttribute("disabled") && currentInput.value !=="" ){
                             nextInput.removeAttribute("disabled");
                             nextInput.focus()
                           }
                      console.log(e);
                     if(e.key === "Backspace")
                     {
                        inputs.forEach((input,index2) => {
                                
                        if(index1 <= index2 && prevInput){

                            input.setAttribute("disabled",true);
                            currentInput.value="";
                            prevInput.focus();
                        }


                        });
                     }

                     if(!inputs[0].disabled && inputs[3].value !==""){
                        button.classList.add("active");
                        return;
                     }
                     button.classList.remove("active");

                });       
             }); 

             window.addEventListener("load",() => inputs[0].focus());
