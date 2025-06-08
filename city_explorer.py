import wikipedia

def get_summary(city):
    try:
        summary = wikipedia.summary(city, sentences=3)
        print(f"\n🧠 Summary for {city}:\n{summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("⚠️ Multiple results found, be more specific:")
        for option in e.options[:5]:
            print(" -", option)
    except wikipedia.exceptions.PageError:
        print("❌ City not found on Wikipedia.")
    except Exception as e:
        print("❌ An error occurred:", e)

if __name__ == "__main__":
    city = input("🌆 Enter a city name: ")
    get_summary(city)
