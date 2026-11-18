import json, csv

with open("data/sample_accident_points.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

features = []
for r in rows:
    features.append({
        "type": "Feature",
        "properties": {
            "id": int(r["id"]),
            "severity": r["severity"],
            "road_name": r["road_name"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [float(r["longitude"]), float(r["latitude"])]
        }
    })

with open("data/sample_accident_points.geojson", "w") as f:
    json.dump({
        "type": "FeatureCollection",
        "features": features
    }, f, indent=2)

print("GeoJSON created:", len(features), "sample points")
