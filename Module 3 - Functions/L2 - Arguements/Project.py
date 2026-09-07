def shutdown(answer):
    if answer == "Yes":
        print("Shutting down")
    elif answer == "No":
        print("Abort shutdown")
    else:
        print("Sorry")

answer = input("Do you want to shut down? ")
shutdown(answer)