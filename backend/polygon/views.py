from rest_framework.generics import ListAPIView, CreateAPIView
from polygon.models import Polygon
from polygon.serializers import PolygonSerializer


class ViewPolygons(ListAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer


class NewCoordinatesPolygons(CreateAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    def perform_create(self, serializer):
        data = self.request.data
        coor = data.get("coordinates")
        serializer.save(coordinates=coor)
        # predict_results = predict_main(coor)
        predict_results = {
            "type": "FeatureCollection",
            "name": "test_aoi_valencia_subpolygon",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            "features": [
                {"type": "Feature", "properties": {"id": 1, "land_cover": "Forest", "land_management": "conservation", "co2_metric_1": 0.15}, "geometry": {"type": "MultiPolygon", "coordinates": [[[[-0.469104334442901, 39.666828826691408 ], [ -0.469104334442901, 39.666828826691408 ], [ -0.456897977701825, 39.637841187874542 ], [ -0.469104334442901, 39.666828826691408 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 2, "land_cover": "Crop 1", "land_management": "intensive", "co2_metric_1": 50.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.464599767315888, 39.656131387015186 ], [ -0.448365190714439, 39.656875361806648 ], [ -0.417678681447144, 39.647774639606659 ], [ -0.417055285932243, 39.637692963085442 ], [ -0.456897977701823, 39.637841187874542 ], [ -0.464599767315888, 39.656131387015186 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 3, "land_cover": "Forest", "land_management": "", "co2_metric_1": -5.23 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.417678681447144, 39.647774639606659 ], [ -0.448365190714439, 39.656875361806648 ], [ -0.464599767315889, 39.656131387015186 ], [ -0.469104334442901, 39.666828826691408 ], [ -0.418862851359067, 39.666925271449202 ], [ -0.417678681447144, 39.647774639606659 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 4, "land_cover": "Crop 1", "land_management": "intensive", "co2_metric_1": 14.02 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.416393774880025, 39.626994874497612 ], [ -0.435594458628075, 39.617317831432395 ], [ -0.44912727506648, 39.61938733418792 ], [ -0.456897977701825, 39.637841187874542 ], [ -0.417055285932243, 39.637692963085442 ], [ -0.416393774880025, 39.626994874497612 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 5, "land_cover": "Forest", "land_management": "", "co2_metric_1": 20.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.44912727506648, 39.61938733418792 ], [ -0.435594458628075, 39.617317831432395 ], [ -0.416393774880025, 39.626994874497612 ], [ -0.415124673301423, 39.606470710813099 ], [ -0.443879593047871, 39.606925146312541 ], [ -0.44912727506648, 39.61938733418792 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 6, "land_cover": "Crop 2", "land_management": "intercropping", "co2_metric_1": 10.5 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.490210232840617, 39.652317010415992 ], [ -0.48548603051501, 39.637947542588819 ], [ -0.515633145142107, 39.638059697403399 ], [ -0.517419117640028, 39.654246773885973 ], [ -0.507394352358076, 39.64900936811032 ], [ -0.490210232840617, 39.652317010415992 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 7, "land_cover": "Forest", "land_management": "", "co2_metric_1": -25.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.494964913764306, 39.66677918410214 ], [ -0.491895606320014, 39.657443361558428 ], [ -0.490210232840617, 39.652317010415992 ], [ -0.507394352358076, 39.64900936811032 ], [ -0.517419117640028, 39.654246773885973 ], [ -0.518796811433409, 39.666733435818898 ], [ -0.494964913764306, 39.66677918410214 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 8, "land_cover": "Forest", "land_management": "", "co2_metric_1": 32.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.482968024864867, 39.63028859856302 ], [ -0.479357097613386, 39.619305346917514 ], [ -0.491501885761712, 39.610103246800158 ], [ -0.514590988945561, 39.628614164462704 ], [ -0.515633145142107, 39.638059697403399 ], [ -0.48548603051501, 39.637947542588819 ], [ -0.482968024864867, 39.63028859856302 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 9, "land_cover": "Forest", "land_management": "", "co2_metric_1": 100.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.479357097613385, 39.619305346917514 ], [ -0.48548603051501, 39.637947542588819 ], [ -0.456897977701825, 39.637841187874542 ], [ -0.449127275066481, 39.61938733418792 ], [ -0.47419044893353, 39.623220114128152 ], [ -0.479357097613385, 39.619305346917514 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 10, "land_cover": "Built-up", "land_management": "", "co2_metric_1": 20.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.479357097613386, 39.619305346917514 ], [ -0.475450936757555, 39.607424091865973 ], [ -0.51231730280016, 39.608006718616899 ], [ -0.514590988945561, 39.628614164462704 ], [ -0.491501885761712, 39.610103246800158 ], [ -0.479357097613386, 39.619305346917514 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 11, "land_cover": "Forest", "land_management": "", "co2_metric_1": 40.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.475450936757555, 39.607424091865973 ], [ -0.479357097613385, 39.619305346917514 ], [ -0.47419044893353, 39.623220114128152 ], [ -0.449127275066481, 39.61938733418792 ], [ -0.448298209786533, 39.617418471127422 ], [ -0.443879593047872, 39.606925146312541 ], [ -0.475450936757555, 39.607424091865973 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 12, "land_cover": "Built-up", "land_management": "", "co2_metric_1": 50.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.490210232840616, 39.652317010415992 ], [ -0.48548603051501, 39.637947542588819 ], [ -0.48548603051501, 39.637947542588819 ], [ -0.490210232840617, 39.652317010415992 ], [ -0.490210232840616, 39.652317010415992 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 13, "land_cover": "Built-up", "land_management": "", "co2_metric_1": -45.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.48548603051501, 39.637947542588819 ], [ -0.490210232840616, 39.652317010415992 ], [ -0.472203890608985, 39.655782916206235 ], [ -0.464599767315889, 39.656131387015186 ], [ -0.456897977701825, 39.637841187874542 ], [ -0.48548603051501, 39.637947542588819 ] ] ] ] } },
                {"type": "Feature", "properties": {"id": 14, "land_cover": "Fallow", "land_management": "", "co2_metric_1": -13.25 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -0.491895606320014, 39.657443361558428 ], [ -0.490210232840616, 39.652317010415992 ], [ -0.490210232840617, 39.652317010415992 ], [ -0.491895606320014, 39.657443361558428 ] ] ] ] } },
                {
                    "type": "Feature",
                    "properties": {
                        "id": 15,
                        "land_cover": "Crop 3",
                        "land_management": "terracing",
                        "co2_metric_1": 17.5
                    },
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [[[
                            [-0.490210232840616, 39.652317010415992],
                            [-0.491895606320014, 39.657443361558428],
                            [-0.494964913764305, 39.66677918410214],
                            [-0.469104334442901, 39.666828826691408],
                            [-0.464599767315889, 39.656131387015186],
                            [-0.472203890608985, 39.655782916206235],
                            [-0.490210232840616, 39.652317010415992]
                            ]]]
                        }
                    }
            ]
        }

        serializer.save(data=predict_results)
