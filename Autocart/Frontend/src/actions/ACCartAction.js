import { GET_CART, UPDATE_CART, DELETE_CART } from "@src/constants";
import { clientRequestWithToken } from "../utils/axioWrapper";
import { asynActionWithToken } from "./actionHelper";

export const getCartList = (countPerPage, curPage, ordering, search) =>
  asynActionWithToken((dispatch, getState) => {
    clientRequestWithToken({
      method: "get",
      url: "/carts/"
    }).then(res => {
      dispatch({
        type: GET_CART,
        payload: res
      });
    });
  });

export const updateCart = (id, obj) =>
  asynActionWithToken((dispatch, getState) => {
    clientRequestWithToken({
      method: "patch",
      url: `/carts/${id}/`,
      data: JSON.stringify(obj)
    }).then(res => {
      dispatch({
        type: UPDATE_CART,
        payload: res
      });
    });
  });

export const removeCart = (id, obj) =>
  asynActionWithToken((dispatch, getState) => {
    clientRequestWithToken({
      method: "delete",
      url: `/carts/${id}/`
    }).then(res => {
      dispatch({
        type: DELETE_CART,
        payload: res
      });
    });
  });