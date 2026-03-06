import typing


def game_event_stream(count: int) -> typing.Generator:
    """
    Generator that creates game events on-demand.
    Doesn't store all events in memory - yields one at a time!
    """
    players = ['alice', 'bob', 'charlie', 'diana']
    event_types = ['killed monster', 'found treasure', 'leveled up']
    
    for i in range(count):
        # Generate event data
        player = players[i % len(players)]  # Cycle through players
        level = (i % 15) + 1  # Levels 1-15
        event = event_types[i % len(event_types)]  # Cycle through events
        
        # YIELD - this is the magic word!
        # Returns this value, then PAUSES until next iteration
        yield {
            'id': i + 1,
            'player': player,
            'level': level,
            'event': event
        }


def fibonacci_generator(limit: int) -> typing.Generator:
    """
    Generator for Fibonacci sequence.
    Perfect example: can generate infinite numbers without storing them!
    """
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a  # Return current Fibonacci number
        a, b = b, a + b  # Calculate next: (1, 0+1), (1, 1+1), (2, 1+2)...
        count += 1


def prime_generator(limit: int) -> typing.Generator:
    """
    Generator for prime numbers.
    Only calculates when you ask for the next one!
    """
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0
    num = 2  # Start checking from 2
    
    while count < limit:
        if is_prime(num):
            yield num  # Return this prime number
            count += 1
        num += 1


def process_stream_with_filter(stream: typing.Generator, min_level: int) -> dict:
    """
    Process a generator stream with filtering.
    Shows how to consume generator data efficiently.
    """
    stats = {
        'total': 0,
        'high_level': 0,
        'treasure_events': 0,
        'levelup_events': 0
    }
    
    # FOR loop automatically calls next() on the generator
    for event in stream:
        stats['total'] += 1
        
        # Filter high-level players
        if event['level'] >= min_level:
            stats['high_level'] += 1
        
        # Count event types
        if 'treasure' in event['event']:
            stats['treasure_events'] += 1
        if 'leveled up' in event['event']:
            stats['levelup_events'] += 1
    
    return stats


def main():
    print("=== Game Data Stream Processor ===")
    
    # Generate 1000 events using a generator
    event_count = 1000
    print(f"Processing {event_count} game events...")
    
    # Create the generator (doesn't generate anything yet!)
    events = game_event_stream(event_count)
    
    # Display first 3 events to show it works
    # Using next() to manually get values
    print(f"Event 1: Player {next(events)['player']} killed monster")
    
    # But we already consumed one! Let's restart
    events = game_event_stream(event_count)
    
    # Show first few events
    for i, event in enumerate(events):
        if i < 3:  # Only show first 3
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['event']}")
        else:
            break  # Stop showing, but generator is still there
    
    # Start fresh for analysis
    print("...")
    print("\n=== Stream Analytics ===")
    
    # Process the entire stream
    events = game_event_stream(event_count)
    stats = process_stream_with_filter(events, min_level=10)
    
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure_events']}")
    print(f"Level-up events: {stats['levelup_events']}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: Minimal")
    
    # Demonstrate other generators
    print("\n=== Generator Demonstration ===")
    
    # Fibonacci sequence
    fib = fibonacci_generator(10)
    fib_numbers = [str(num) for num in fib]  # Consume generator into list
    print(f"Fibonacci sequence (first 10): {', '.join(fib_numbers)}")
    
    # Prime numbers
    primes = prime_generator(5)
    prime_numbers = [str(num) for num in primes]
    print(f"Prime numbers (first 5): {', '.join(prime_numbers)}")


if __name__ == "__main__":
    main()