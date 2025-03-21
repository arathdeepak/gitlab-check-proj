dependency_tree = {
    'merit2-common': [],
    'web-sso': ['merit2-common'],
    'tradersbook-fincad': ['merit2-common'],
    'tradersbook-mt-vrdo-processor': ['merit2-common'],
    'secmaster-mt': ['merit2-common'],
    'admin-mt': ['merit2-common'],
    'ctm-eisl-service': ['merit2-common'],
    'tradersbook-instrument-store': ['merit2-common', 'tradersbook-fincad'],
    'secmaster-ui': ['merit2-common', 'secmaster-mt'],
    'admin-ui': ['merit2-common', 'admin-mt'],
    'trade-processor-ctm': ['merit2-common', 'ctm-eisl-service'],
    'tradersbook-venue-connector': ['merit2-common', 'tradersbook-mt-vrdo-processor'],
    'secmaster-etl': ['merit2-common', 'tradersbook-instrument-store'],
    'tradersbook-mt': ['merit2-common', 'tradersbook-instrument-store'],
    'cbw-mt-springboot': ['merit2-common', 'tradersbook-instrument-store'],
    'msrb-realtime-trade-webapi': ['merit2-common', 'tradersbook-instrument-store'],
    'tradersbook-ui': ['merit2-common', 'tradersbook-mt'],
    'tradersbook-order-processing': ['merit2-common', 'tradersbook-mt'],
    'cbw-ui': ['merit2-common', 'cbw-mt-springboot']
}

def generate_waves(start_component):
    waves = []
    current_component = start_component
    while current_component in dependency_tree:
        wave = [current_component]
        dependencies = dependency_tree[current_component]
        for component in dependencies:
            if component in dependency_tree:
                wave.append(component)
        waves.append(wave)
        if dependencies:
            current_component = dependencies[0]
        else:
            break
    return waves

# Get the start component as input parameter
import sys

if len(sys.argv) < 2:
    print("Please specify a start component as a parameter.")
else:
    start_component = sys.argv[1]
    waves = generate_waves(start_component)
    
    for i, wave in enumerate(waves, start=1):
        print(f"Wave {i}: {', '.join(wave)}")
