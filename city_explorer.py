import wikipedia

def get_summary(city):
    try:
        wikipedia.set_lang("en")  # Or use "fr" if you want French content

        # Attempt to fetch the page directly by title
        try:
            page = wikipedia.page(city + " (city)")
            summary = page.summary[:500]  # Limit to 500 characters for brevity
            print(f"\n🧠 Summary for {page.title}:\n{summary}")
            return
        except wikipedia.exceptions.DisambiguationError as e:
            print("⚠️ Too many results. Try to be more specific. Example options:")
            for option in e.options[:5]:
                print(" -", option)
            return
        except wikipedia.exceptions.PageError:
            print(f"❌ No specific page found for '{city}'. Trying search results...")

        # Fallback to search if direct page fetch fails
        search_results = wikipedia.search(city)
        if not search_results:
            print("❌ No results found for", city)
            return

        best_match = search_results[0]
        print(f"🔎 Best match found: {best_match}")

        # Fetch summary from the best match
        summary = wikipedia.summary(best_match, sentences=3)
        print(f"\n🧠 Summary for {best_match}:\n{summary}")

    except wikipedia.exceptions.PageError:
        print("❌ Page not found.")
    except Exception as e:
        print("❌ An unexpected error occurred:", e)

if __name__ == "__main__":
    city = input("🏙️ Enter a city name: ")
    get_summary(city)
