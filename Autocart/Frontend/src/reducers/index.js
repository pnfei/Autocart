import Auth from "./ACAuthReducer";
import Pagination from "./PaginationReducer";
import Cart from "./ACCartReducer";
import { combineReducers } from "redux";

export default combineReducers({
  Auth,
  CarList: Pagination("CarList", {
    count: 0,
    list: [],
    curPage: 1,
    countPerPage: 10,
    filters: {
      ordering: "-year",
      brand: [],
      category: [],
      search: "",
      price__gte: "",
      price__lte: ""
    }
  }),
  Cart
});
