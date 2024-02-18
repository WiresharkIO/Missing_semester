import requests
import argparse

# function uses argparse to get the server URL and API key from the CLI.
def parse_arguments():

	# if no default option present for particulars, pass it through command in CLI..
	parser = argparse.ArgumentParser(description="Chat with Llama AI")
	parser.add_argument("server_url", help="URL of the Llama server")
	parser.add_argument("--api_key", help="API key for the Llama server")
	parser.add_argument("--port", type=int, default=8080, help="Port number for the server")
	parser.add_argument("--mode", choices=["helpful", "playful"], default="helpful", help="Chat mode")
	parser.add_argument("--temperature", type=float, default=0.8, help="controlling creativity")
	return parser.parse_args()

def send_message(server_url, api_key, message, temperature, mode):

	headers = {"Authorization": f"Bearer {api_key}"}
	#data = {"message": message, "temperature": temperature, "mode": mode}
	data = {"prompt": message, "temperature": temperature, "mode": mode}
	response = requests.post(server_url, headers=headers, json=data)
	#response = requests.post(server_url, headers=headers, json=data)
	
	# to handle server response status code
	if response.status_code == 200:
		#return response.json()["response"]
		return response.json()["content"]
	# no response
	else:
		raise Exception(f"Error sending message: {response.status_code} - {response.text}")

def call_sequence():
	  args = parse_arguments()
	  server_url = f"http://localhost:{args.port}/completion"
	  api_key = args.api_key
	  mode = args.mode
	  temperature = args.temperature
	  
	  # Store recent conversation
	  history = []  

	  # first instructuion to tell about the mode..
	  initial_instruction = f"[INST] You are a chatbot in {mode} mode. [/INST]"
	  history.append(initial_instruction)

	  # if API KEY was not there or not given properly this prints..
	  if not api_key:
	  	print("API key is not therrre")
	  	return

	  print(" !!! Llama chat !!!, Type 'help' for help or 'exit' to quit.")
	  
	  
	  while True:
	  	message = input("> ")
	  	
	  	# To EXIT!!!
	  	if message == "exit":
	  		break
	  		
	  	# FOR HELP!!!
	  	elif message == "help":
	  		print("\nYou can use the following commands here:")
	  		print("- help: don't fall for recursion.")
	  		print("- exit: Quit the environment.")
	  		print("- history: recent conversation..")
	  		
	  	elif message == "history":
	  		if history:
	  			print("\nConversation history:")
	  			print(*history, sep="\n")
	  			
	  	else:
	  		response = send_message(server_url, api_key, message, temperature, mode)
	  		history.append(f"[INST] You: {message} [/INST]\n[INST] Llama ({mode}): {response} [/INST]")
	  		print(f"Llama ({mode}): {response}")

if __name__ == "__main__":
	print("Hallo!!")
	call_sequence()
	print("Tschüss!!")

	
	
