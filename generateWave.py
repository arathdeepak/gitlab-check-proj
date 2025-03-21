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

wave_definitions = {
    'wave1': ['merit2-common'],
    'wave2': ['web-sso', 'tradersbook-fincad', 'tradersbook-mt-vrdo-processor', 'secmaster-mt', 'admin-mt', 'ctm-eisl-service'],
    'wave3': ['tradersbook-instrument-store', 'secmaster-ui', 'admin-ui', 'trade-processor-ctm', 'tradersbook-venue-connector'],
    'wave4': ['secmaster-etl', 'tradersbook-mt', 'cbw-mt-springboot', 'msrb-realtime-trade-webapi'],
    'wave5': ['tradersbook-ui', 'tradersbook-order-processing', 'cbw-ui']
}

def generate_waves(start_component):
    waves = []
    current_component = start_component
    for wave, components in wave_definitions.items():
        if current_component in components:
            waves.append((wave, components))
            current_component = components[-1]
    return waves

# Get the start component as input parameter
import sys

if len(sys.argv) < 2:
    print("Please specify a start component as a parameter.")
else:
    start_component = sys.argv[1]
    waves = generate_waves(start_component)
    
    for wave, components in waves:
        print(f"wave{wave}: {', '.join(components)}")
